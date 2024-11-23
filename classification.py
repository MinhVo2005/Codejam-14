import os
import json

class Calculations:


    
    def load_results(self, filename):
        """Load previously saved results from a JSON file."""
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.fruits_and_vegetables = data.get('fruits_and_vegetables', {})
                self.protein = data.get('protein', {})
                self.grains = data.get('grains', {})
        else:
            # If the file does not exist or is empty, initialize empty dictionaries
            self.fruits_and_vegetables = {}
            self.protein = {}
            self.grains = {}

    def save_results(self, filename):
            """Save current results to a JSON file."""
            data = {
                'fruits_and_vegetables': self.fruits_and_vegetables,
                'protein': self.protein,
                'grains': self.grains
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)  # Save data in a readable format

    def __init__(self):
            self.fruits_and_vegetables= {} 
            self.protein={}
            self.grains={}

    def addDictionary(self, i, dic, gr):  # Add self here
            # Corrected to use the key as a string instead of a set
            key = gr[i][0]  # Get the item name from the tuple
            val = dic.get(key)  # Retrieve the current count

            if val is None:
                dic[key] = 1  # Initialize count if the item is not in the dictionary
            else:
                dic[key] = val + 1  # Increment count if the item already exists

    def classify(self, groupings):
            for i in range(len(groupings)):
                if len(groupings[i]) ==3:
                    if groupings[i][1] == "Vegetable":
                        self.addDictionary(i, self.fruits_and_vegetables, groupings)
                    elif groupings[i][1] == "Protein":
                        self.addDictionary(i, self.protein, groupings)
                    elif groupings[i][1] == "Grains":
                        self.addDictionary(i, self.grains, groupings)

    def resetJson(self,filename):
        with open(filename, 'w') as f:
            json.dump({}, f)



# Example usage
if __name__ == "__main__":
    filename = 'results.json'
    
    # Create a new instance of Calculations
    cal = Calculations()
    
    # Load existing results from the JSON file or initialize empty dictionaries
    cal.load_results(filename)

    # New groupings to classify
    new_groupings = [
        ("banana", 'Vegetable', 0.6),
        ("chicken", 'Protein', 0.9),
        ("ryeBread", 'Grain', 0.95),
        ()  # This will update the count for apple
    ]

    # Classify the new groupings
    cal.classify(new_groupings)

    # Save the updated results back to the JSON file
    cal.save_results(filename)

    # Print the updated categorized results
    print("Fruits and Vegetables:", cal.fruits_and_vegetables)
    print("Protein:", cal.protein)
    print("Grains:", cal.grains) 
