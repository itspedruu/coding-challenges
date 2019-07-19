## 100 Doors

Thera are 100 doors in a row that are initially closed. You make 100 passes by the doors. In the first time, you visit every door and toogle the door (if the door is closed you open and if the door is open you close). The second time, only visit every 2nd door (2, 4, 6, ...) and toogle it. The third time, only visit every 3rd door (3, 6, 9, ...). And so on until you only visit the 100th.

**Problem:** Determinate how many doors are open and closed and indicate them after the last pass.

**Conclusions from the solution:** Only the doors with perfect root squares end up open after the last pass.

**My solution discussion:** Of course there are many better ways to execute the problem after knowing that only root squares end up open after the last pass, but starting from the point you don't know if they are open or closed we need to loop throughout each one and check if they are open or closed.