# middleman
a trusted machine that does things for you and other people
inspired by Ether

# how it works
Middleman is essentially a robot that we have written together. We agree on every capability that we decide to give it. It can then automate things like chore assignment (according to an agreed schedule), recurring payments, a house crypto-trading-bot, and one-time actions that would be easier to do with code.

To add a capability to the robot:
1. define an capability blueprint (a python function) in `actions/`
2. "add" the capability to the robot (with consensus). Consensus is achieved by a shared ledger (the list of machine processes that were started/stopped). For anything to be put on the ledger, all co-stake-holders must sign off on it. For now, we assume automatic sign-off.

In addition, we can "remove" capabilities from the robot (also by logging an entry in the ledger). At any point in time, the state of the robot can be reconstructed.

Finally, we are building a web UI to view the state of the robot (who is taking out the trash today? how much does mic owe ben because of spotify?). This web UI can also add/remove capabilities to the robot (e.g. automated one time actions like "turn off the internet-controlled lights"

# determinism
all machine code must have deterministic effects on the state

# state dump
the machine also dumps its state periodically for readability. The state is, however, rederivable from the ledger and executing the machine in a deterministic way. The ledger/state dump/actions remain private to the group of people using the machine. Expect this repo to be made private soon.

# machine running
right now, every minute, the machine executes the set of "currently running code" (a list of function calls). A function doesn't necessarily have to remove itself from the list.

# possible ledger actions

```
  ADD(charge_spotify_monthly(args))  -> returns an PROCESS_ID
  REMOVE(PROCESS_ID)
  ADD_RUNONCE_REMOVE(pay_person(kai, 20))  -> only want this to run once
```

Each of these ledger actions requires consensus.
Another interesting side effect is that once a ledger action has been added to the ledger, it can no longer be redefined. You can remove it from the machine and add a new version, but you cannot remove the code; otherwise we can no longer reconstruct the state from history. (though it would be a cool project to integrate git)


