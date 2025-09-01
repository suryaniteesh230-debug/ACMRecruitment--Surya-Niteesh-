# Process Detective Notes

## Start the process
Command: `sleep 100 &`  
- Runs a sleep process in the background.  
- PID shown .

## Detect the process
Commands: 
- `ps aux | grep sleep`  
- `pgrep -l sleep`  
- `top` (search for sleep)  

## Terminate the process
Command: `kill' 
- Verifies the process has stopped using `ps aux | grep sleep`.
