The following notes are some disjoint, messy bullets from https://github.com/SpoonLabs/coming

---
- The `-mode` flag is used to indicate the *analyzer* to be used. For example `-mode mineinstance` detects *instances* of a change pattern.
	You can mind simple changes (i.e. exactly one change) with the following command.
	```sh
	# Note the flags {-mode, -action, -entitytype}
	java -classpath ./coming.jar fr.inria.coming.main.ComingMain -location  ./repogit4testv0/ -mode mineinstance -action INS -entitytype BinaryOperator   -output ./out
	```