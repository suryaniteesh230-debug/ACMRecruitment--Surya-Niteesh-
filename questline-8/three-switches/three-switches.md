# Three Switches Puzzle Solution

**Task:**  
You have 3 switches in one room. Only one of them controls a bulb in another room. You may enter the bulb room only once. Determine which switch controls the bulb.

---

## Strategy

1. Turn **Switch 1** ON and leave it on for a few minutes.  
2. After a few minutes, turn **Switch 1** OFF and turn **Switch 2** ON.  
3. Leave **Switch 3** OFF.  
4. Enter the bulb room (only once):
   - If the bulb is **ON**, the correct switch is **Switch 2**.  
   - If the bulb is **OFF but warm**, the correct switch is **Switch 1**.  
   - If the bulb is **OFF and cold**, the correct switch is **Switch 3**.  

---

## Logic

This works because the bulb not only shows its **current state** (on/off) but also retains **heat** for a short time after being turned off.  
- Warm bulb = recently powered = Switch 1.  
- On bulb = currently powered = Switch 2.  
- Cold bulb = never powered = Switch 3.  
