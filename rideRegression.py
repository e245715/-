class RideRegression(LinearRegression):
    alpha =None
    
    def _init_(self,alpha=0.1):
        self.alpha = alpha
        
    def fit(self,input,output):
        pass