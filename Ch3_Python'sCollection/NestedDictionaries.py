#nested dictionaries 
#here we have a dictionary phone and it has another dictionaries area1 and area2 in them
phone= {
         "Area1": {
         "a":0,"b":1,"c":2,"d":3
         },
       
         "Area2": {
            "x":10,"y":20,"z":30
         }
       }
print(phone["Area1"]["a"])  #printing number corresponding to "a " in Area1
print(phone["Area2"]["x"]) 