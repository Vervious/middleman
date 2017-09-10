# middleman
a trusted machine that does things for you and other people
inspired by Ether

# how it works
for something to be added to the ledger (the list of machine code/processes that were run/started), everyone must have signed off on it happening (global concensus).

# determinism
all machine code must have deterministic effects on the state

# state dump
the machine also dumps its state periodically for readability. The state is, however, rederivable from the ledger and executing the machine in a deterministic way.

# machine running
right now, every minute, the machine executes the set of "currently running code" (a list of function calls). A function doesn't necessarily have to remove itself from the list.

# possible ledger actions

  ADD(charge_spotify_monthly(args))  -> returns an PROCESS_ID
  REMOVE(PROCESS_ID)
  ADD_RUNONCE_REMOVE(pay_person(kai, 20))  -> only want this to run once

Each of these ledger actions requires consensus
