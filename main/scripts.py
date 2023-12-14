import string
class ExcelHelper:
    # Considering that the file has been validated
    def __init__(self, sheet):
        self.sheet = sheet
        self.images = []
        
        sheet_images = sheet._images
        for image in sheet_images:
            # Considering We have a head the row is deducted for easier use
            row = image.anchor._from.row-1
            # we are storing col as an indicator of which answer option it is. 
            col = string.ascii_uppercase[image.anchor._from.col+1]
            
            image_dict = {
                "row": int(row),
                "col" : str(col),
                "image": image._data
            }
            self.images.append(image_dict)   
    
    # returns image data by filtering through
    def locate_image(self, row, col):
        for image_dict in self.images:
            if image_dict['row'] == row and image_dict['col'] == col:
                return image_dict['data']
        return False
    
    # this method returns all the options with images in a row
    def get_cols_by_row(self, row):
        cols = []
        for image_dict in self.images:
            if image_dict['row'] == row:
                cols.append(image_dict['cols'])
        cols.sort()
        return cols
    
    # this method returns all the rows with image in it
    def get_all_rows(self):
        rows = []
        for image_dict in self.images:
            rows.append(image_dict['row'])
        rows.sort()
        return rows  
    
    
    def get_all_cols(self):
        cols = []
        for image_dict in self.images:
            cols.append(image_dict['col'])
        return cols 
    
    @property
    def has_image(self):
        return True if self.images else False