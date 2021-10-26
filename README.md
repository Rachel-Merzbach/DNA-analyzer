# DNA analyzer : Rachel Merzbach

## GOAL ##
The goal of the system is to load, analyze, manipulate and save DNA sequences.


## DESCRIPTION ##
The system interact with the user through a CLI (Command Line Interface) that uses the standard I/O.
Using that interface, the user can load DNA sequences from files, analyze them, manipulate them (e.g., by extracting
sequence slices or by modifying the sequence), and store modified sequences.


## PROJECT FLOW ##

*Design patterns:*

For managing all the input and output streams I used `CMD` class. this class inherits the `CLI` class, which is SingleTone.
contains only the function exe()

Each type of command (Creating, Manipulating, Management, Batch, Analysis) has a different directory, and each command has a different class, which manages it.
Each command's class inherits the `command` class (unless the Batch commands). this class contains the functions __init__(), process() and execute(), and every command implements these functions.

For managing the commands, there is a factory named `commandsFactory`. this class initial the required command in the __init__() and create a new command in the create_command() 

For managing the DB I used SingleTone class - `commandsDB`. now each class of command can use the DB concurrently.

For managing the batch commands I created `BATCH` class. it has __init__() and execute()
All the batch commands use the `batchDB` which is SingleTone.

The DataBase use `DnaSequence` to store all the dna sequences.



*Implementd Commands:*


### Creation Commands: new, load and dup are described below, along with form of use.

new <sequence> [@<sequence_name>] 
Creates a new sequence. If the ​[@<sequence_name>] is given, then this will be the name of the new sequence, Otherwise, a default name will be provided. The new sequence, its name and its number are printed.

load <file_name> [@<sequence_name>] 
loads the sequence from the given file, assigns it with a number (ID) and a default name, if [@<sequence_name>] was not provided, and prints it.

dup <seq> [@<new_seq_name>]
duplicates the sequence. If [@<new_seq_name>] is not provided, then the new sequence name will be based on the name of ​<seq>.

 
### Manipulating Commands: slice and replace are described below, along with form of use.

slice <seq> <from_ind> <to_ind> [: [@<new_seq_name>|@@]]
Slices the sequence, so that starts in <from_ind> and ends in <to_ind>.
If [@<new_seq_name>] is provided, the results will create a new sequence with that name.
If [@@] is provided, the results will create a new sequence with auto-generate name, based on the name of the original sequence.
 
replace <seq> <index> <new_letter> [: [@<new_seq_name>|@@]]
If [​@<new_seq_name>] is provided, the original sequence is left untouched and the result is put in a newly created sequence with that name.
If ​[@@] is provided, the name is based on the original sequence.
The command might get more than a single replacement. In that case, after ​<seq> there will be more than one pair of ​<index> and ​<new_letter>

 
### Analysis Commands: find and findall are described below, along with form of use.
 
find <seq> <expressed_sub_seq> | find <seq_to_find_in> <seq_to_be_found>
Returns the index of the first appearance of <expressed_sub_seq> in <seq>
Or returns the first appearance of <seq_to_be_found> in <seq_to_find_in>, Depending on the data obtained
                                                              
findall <seq_to_find_in> <seq_to_be_found> | findall <seq> <expressed_sub_seq> 
Returns all the indices of appearances of <expressed_sub_seq> in <seq>
Or returns all the indices of appearances of <seq_to_be_found> in <seq_to_find_in>, Depending on the data obtained


### Management Commands: del and save are described below, along with form of use.

del <seq>
deletes that sequence.
Before deleting it, the user is asked to confirm that: Confirmation is done by entering y or Y, Entering n or N cancels the deletion.
Once confirmed, the sequence is deleted and a message is printed. Otherwise, a cancellation message is printed.

save <seq> [<filename>]
saves sequence <seq> to a file. If [<filename>] is not provided, the sequence name is being used. The filename is suffixed by .rawdna


### Batch Commands: batchshow, batchlist and run are described below, along with form of use.
 
batchshow <batch_name>
This command shows the content of that batch.

run <batchname> 
Runs a batch, that is, executes it as if the commands were entered manually.
 
batchlist
Shows a list of all the batch names
