import ffx.potential.MolecularAssembly
import ffx.potential.bonded.Atom
import ffx.potential.cli.PotentialScript
import ffx.potential.parsers.XYZFilter
import picocli.CommandLine

import static ffx.numerics.math.DoubleMath.length
import static ffx.numerics.math.DoubleMath.sub
import static java.lang.String.format

@CommandLine.Command(description = "FindMinIonDistance takes in a structural archive file and determines the minimum distance between restrained atoms for each snapshot", name = "ffxc FindMinIonDistance")
class FindMinIonDistance extends PotentialScript {

    /**
     * The final argument should be an archive file
     */
    @CommandLine.Parameters(arity = "1", paramLabel = "files",
            description = 'file(s).')
    private List<String> filenames = null

    /**
     * Execute the FindMinIonDistance script.
     */
    @Override
    FindMinIonDistance run() {

        if (!init()) {
            return
        }

        // Read in archive file
        MolecularAssembly molecularAssembly
        XYZFilter xyzFilter
        try {
            molecularAssembly = potentialFunctions.open(filenames.get(0))
            xyzFilter = (XYZFilter) potentialFunctions.getFilter()
        } catch (IOException e) {
            logger.warning("Could not read input trajectory file")
            e.printStackTrace()
        }

        // Get collection of restrained atom pairs
        // Add restrain-bond records. If no restrain-distance records exist, the empty array will be
        // returned.
        String[] bondRestraints = molecularAssembly.getProperties().getStringArray("restrain-distance")
        double overallMinDistance = 2000.0

        // Use xyzFilter.readNext() to advance coords and read next file in archive
        while(xyzFilter.readNext()){
            Atom[] snapshotAtoms = molecularAssembly.getAtomArray()
            double min = 2000.0
            Atom minatom1
            Atom minatom2
            // Go through restrained atoms - find the minimum distance between any two and report it for the snapshot
            for(String bondRest : bondRestraints){
                try {
                    String[] toks = bondRest.split("\\s+")
                    if (toks.length < 2) {
                        throw new IllegalArgumentException(
                                format(" restrain-distance value %s could not be parsed!", bondRest))
                    }
                    // Internally, everything starts with 0, but restrain distance starts at 1, so that 1 has to
                    // be subtracted
                    int at1 = Integer.parseInt(toks[0]) - 1
                    int at2 = Integer.parseInt(toks[1]) - 1
                    Atom a1 = snapshotAtoms[at1]
                    Atom a2 = snapshotAtoms[at2]

                    double[] a1coords = new double[3]
                    double[] a2coords = new double[3]
                    double[] distDiff = new double[3]

                    a1.getXYZ(a1coords)
                    a2.getXYZ(a2coords)

                    sub(a1coords,a2coords,distDiff)
                    double len = length(distDiff)

                    if (len < min){
                        min = len
                    }

                } catch (Exception ex) {
                    logger.info(format(" Exception in parsing restrain-distance: %s", ex))
                }
            }
            logger.info(format("Minimum distance between restrained ion and phosphorous in current snapshot %4.3f", min))
            if (min < overallMinDistance){
                overallMinDistance = min
            }
        }
        logger.info(format("\nMinimum across trajectory %4.3f",overallMinDistance))
        return this
    }
}
