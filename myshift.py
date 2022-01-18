from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4 as uuid

app = FastAPI()

shiftlist = []

#Shift Model
class shiftbase(BaseModel):
    id: str
    name: str
    start: str
    end: str
    pause: str
    active: bool = True

@app.get('/') 
async def root():
    return "Welcome to my Shift"

@app.get('/shifts')
async def get_shifts():
    return shiftlist

@app.post('/shifts')
async def save_shifts(shifts: shiftbase):
    shifts.id = str(uuid())
    shiftlist.append(shifts)
    return shiftlist[-1]
 
@app.get('/shifts/{shift_id}')
async def get_shifts(shift_id: str):
    for shifts in shiftlist:
        if shifts.id == shift_id:
            return shifts
    raise HTTPException(status_code=404, detail="does not exist")

@app.delete("/shifts{shift_id}")
async def delete_shifts(shift_id: str):
    for index, shifts in enumerate(shiftlist):
        if shifts.id == shift_id:
            shiftlist.pop(index)
            return "post has been deleted successfully"
    raise HTTPException(status_code=404, detail="does not exist")

@app.put('/shifts/{shift_id}')
async def update_shifts(shift_id: str, updateshifts: shiftbase):
    for index, shifts in enumerate(shiftlist):
        if shifts.id == shift_id:
            shiftlist[index].name = updateshifts.name
            shiftlist[index].start = updateshifts.start
            shiftlist[index].end = updateshifts.end
            shiftlist[index].pause = updateshifts.pause
            shiftlist[index].active = updateshifts.active
            return "post has been updated successfully"
    raise HTTPException(status_code=404, detail="does not exist")





