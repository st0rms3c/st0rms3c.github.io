import copy
import glob
import hashlib
import time
import os

def main():
    old_hashes = {}
    new_hashes = {}
    
    while True:
        old_hashes = copy.deepcopy(new_hashes)
        
        for file in ["portable.php", "style.css", "prism.css", "prism.js"]:
            new_hashes[file] = hashlib.sha512(open(file, "rb").read()).hexdigest()
        
        for file in glob.glob("dependencies/*.php"):
            new_hashes[file] = hashlib.sha512(open(file, "rb").read()).hexdigest()
        
        for file in glob.glob("content/*.md"):
            new_hashes[file] = hashlib.sha512(open(file, "rb").read()).hexdigest()
            
        for file in glob.glob("content/_extra/*.md"):
            new_hashes[file] = hashlib.sha512(open(file, "rb").read()).hexdigest()
    
        update = False
    
        for item in new_hashes:
            if item not in old_hashes:
                update = True
                break
                
            if new_hashes[item] != old_hashes[item]:
                update = True
                break
                
        if update == True:
            print("Updating")
            os.system("php portable.php > index.html")
    
        time.sleep(0.1)

if __name__ == "__main__":
    main()
    