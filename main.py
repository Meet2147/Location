from fastapi import FastAPI
from fastapi.responses import FileResponse
import instaloader
from glob import glob
import os
from PIL import Image
from starlette.responses import StreamingResponse
from starlette.requests import Request
from geopy.geocoders import Nominatim



app = FastAPI()


@app.get("/")
def root():
  return {"Welcome": "Hello, World"}

@app.get("/location/")
def profile(location: str):
    geolocator = Nominatim(user_agent="location_api")
    loc = geolocator.geocode(f"{location}")
    address = loc.address
    lat = loc.latitude
    lng = loc.longitude
    loc_type = loc.raw['class']
    return {"address": address, "latitude": lat, "lng": lng, "type": loc_type}
    
    