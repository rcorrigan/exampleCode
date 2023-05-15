import ffx.potential.cli.PotentialScript
import org.apache.commons.io.FilenameUtils
import picocli.CommandLine

import java.awt.image.BufferedImage

@CommandLine.Command(description = "WriteGroupRestraints takes in a file and writes group restraints between P and ions", name = "ffxc WriteGroupRestraints")
class WriteGroupRestraints extends PotentialScript {

    /**
     * * --min or --minDist The minimum allowable distance restraint value
     */
    @CommandLine.Option(names = ['--min', '--minDist'], paramLabel = "0", defaultValue = "5.0",
            description = 'The minimum allowable distance restraint value.')
    private double minDist = 5.0

    /**
     * * --max or --maxDist The maximum allowable distance restraint value
     */
    @CommandLine.Option(names = ['--max', '--maxDist'], paramLabel = "0", defaultValue = "45.0",
            description = 'The maximum allowable distance restraint value.')
    private double maxDist = 45.0

    /**
     * * -r or --restraintStrength The restraint strength
     */
    @CommandLine.Option(names = ['-r', '--restraintStrength'], paramLabel = "0", defaultValue = "10.0",
            description = 'The maximum allowable distance restraint value.')
    private double restraintStrength = 10.0

    /**
     * The final argument(s) should be one or more filenames.
     */
    @CommandLine.Parameters(arity = "1", paramLabel = "files",
            description = 'file(s).')
    private List<String> filenames = null

    List<String> groups = new ArrayList<>()
    List<String> restrainGroups = new ArrayList<>()
    List<String> phosphorousAtoms = new ArrayList<>()
    List<String> ions = new ArrayList<>()

    /**
     * Execute the WriteGroupRestraints script.
     */
    @Override
    WriteGroupRestraints run() {

        if (!init()) {
            return
        }

        // Read in XYZ or PDB file
        String fileExtension = FilenameUtils.getExtension(filenames.get(0))
        logger.info("File extension: " + fileExtension)
        try {
            BufferedReader structureFileReader = new BufferedReader(new FileReader(filenames.get(0)))
            String line

            while ((line = structureFileReader.readLine()) != null) {
                String[] splitLine = line.split("\\s+")
                if (fileExtension.contains("pdb") && (line.contains("ATOM") || line.contains("HETATM"))) {
                    if (line.contains(" P ")) {
                        // Save to phosphates location
                        phosphorousAtoms.add(splitLine[1])
                    } else if (line.contains("NA") || line.contains("K") || line.contains("MG") || line.contains("CL")) {
                        // Save to ions location
                        if(line.contains('HETATM ')) {
                            ions.add(splitLine[1])
                        } else{
                            String start = splitLine[0]
                            start = start.replaceAll("[A-Z]","")
                            ions.add(start)
                        }
                    }
                } else if (fileExtension.contains("xyz")) {
                    if (line.contains(" P ")) {
                        // Save to phosphates location
                        phosphorousAtoms.add(splitLine[1])
                    } else if (line.contains("Na+") || line.contains("K+") || line.contains("Mg+") || line.contains("Cl-")) {
                        // Save to ions location
                        ions.add(splitLine[1])
                    }
                }
            }
        } catch (IOException e) {
            logger.warning("Could not read input structure file")
            e.printStackTrace()
        }
        // Write out group and restrain-groups strings
        String moleculeName = FilenameUtils.removeExtension(filenames.get(0))
        FileWriter groupFileWriter = new FileWriter(moleculeName + ".groups.txt")
        int phosGroupCounter = 1
        for (String phosphorous : phosphorousAtoms) {
            String groupLine = "group " + phosGroupCounter.toString() + " " + phosphorous
            groupFileWriter.write(groupLine + "\n")
            phosGroupCounter++
        }
        int ionGroupCounter = phosGroupCounter
        for (String ion : ions) {
            String groupLine = "group " + ionGroupCounter.toString() + " " + ion
            groupFileWriter.write(groupLine + "\n")
            ionGroupCounter++
        }
        for (int j = 1; j < phosGroupCounter; j++) {
            for (int k = phosGroupCounter; k < ionGroupCounter; k++) {
                String restrainGroupsLine = "restrain-groups " + j.toString() + " " + k.toString() + " " +
                        restraintStrength + " " + minDist + " " + maxDist
                groupFileWriter.write(restrainGroupsLine + "\n")
            }
        }
        for(String phosphorous : phosphorousAtoms){
            for(String ion : ions){
                String restrainDistLine = "restrain-distance "+ phosphorous + " " + ion + " " +
                        restraintStrength + " " + minDist + " " + maxDist
                groupFileWriter.write(restrainDistLine + "\n")
            }
        }
        groupFileWriter.close()
    }
}
