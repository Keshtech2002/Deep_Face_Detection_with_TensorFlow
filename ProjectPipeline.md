1. SEt up dependencies
    - !pip install labelme albumentations
    - !pip install tensorflow-gpu tensorflow matplotlib opencv-python
2. Collect Images
    - Create ```data``` folder containg ```images``` and ```labels``` folders
    - Collect images
3. Annotate
    - Use ```labelme``` to annotate
    - Just type ```labelme``` on the command line or ```!labelme``` on jupyter to open
4. Partition Data
    - Manually split data into train, test, validation set
    - create respective folders in the data directory
    - inside the ```train```, ```test```, ```val```, folders create ```images``` and ```labels``` folder
    - Move images into the folders in this project (63 to train, 14 to test, 13 to val)