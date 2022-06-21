class Report():

    def __init__(self,test_results=[]):
        self.test_results = test_results

    #count how many times an item appears in an array
    def count_results(self):
        green_count = self.test_results.count("Green")
        #red_count = self.test_results.count("Red")
        amber_count = self.test_results.count("Amber")
        return f"Green: {green_count}\n Amber:{amber_count}"

        

