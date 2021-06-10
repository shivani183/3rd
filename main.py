class Items:
    itemname:str
    itemcode:str

    def createItems(self):
        #we will do this portion later
        print("itemcode : " + self.itemcode)
        print("itemname : " + self.itemname)
        print("Item created")

objItems=Items()
objItems.itemname="Sugar"
objItems.itemcode="67890"

objItems.createItems()




