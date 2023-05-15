These files are set up as examples of Groovy scripts. They are designed to be run as a part of Force Field X (FFX, https://github.com/SchniedersLab/forcefieldx)

This example walks through determining the minimum distance between ions and phosphorous atoms in each snapshot of the 1zih.arc structural archive file. First, the WriteGroupRestraints.groovy file can be run to set up restraints between ions and phosphorous atoms:

ffxc WriteGroupRestraints.groovy 1zih.xyz

The above command produces a file named '1zih.groups.txt' that has syntax for either using 'group' + 'restrain-groups' keywords or 'restrain-distance' keywords to restrain all ions to all phosphorous atoms in the input file.
There are three flags available in the WriteGroupsRestraints.groovy script (listed when using ffxc WriteGroupRestraints.groovy -h):
--min or --minDist : the minimum distance to all ions to get to phosphorous atoms in a molecule
--max or --maxDist : the maximum distance any ion can be from any phosphorous atom in a molecule
-r or --restraintStrength : the strength of the flat-bottom harmonic potential restraint to impose when an ion attempts to violate the established distance restraints during molecular dynamics (MD) simulations

Flags are added to a groovy script as such:

ffxc WriteGroupRestraints.groovy --min 5.0 --max 50.0 -r 20.0 1zih.xyz

The above command would write out restrints that prevented ions from getting within less than 5.0 Angstroms of any phosphorous atom or further than 50.0 Angstroms from any phosphorous atom with a strength of 20.0 kcal/mol

The prefered keywords (either 'group' + 'restrain-groups' lines or 'restrain-distance' lines) produced by the WriteGroupRestraints.groovy script can then be added to the 1zih.key file (an example set has already been added in this case)
These keywords will restrain ions during molecular dynamics simulations and, in this example, feed into the FindMinIonDistance script calculations.

The FindMinIonDistance.groovy script can then be run on the example MD trajectory, 1zih.arc:

ffxc FindMinIonDistance.groovy 1zih.arc

The above command will print out the minimum distance between any ion and any phosphorous in each snapshot in the 1zih.arc file. The current example files will produce results as shown in the 'minIonDistances.log' file
