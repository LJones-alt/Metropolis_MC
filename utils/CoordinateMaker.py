class CoordinateHandler:
    def __new__(ch, a):
        handler = super().__new__(ch)
        return handler

    def __init__(self, a):
        self.a = a
        self.a1=[0,0,0]
        self.a2=[(self.a/((2)**0.5)),0,(self.a/((2)**0.5))]
        self.a3=[(self.a/((2)**0.5)),(self.a/((2)**0.5)),0]
        self.a4=[self.a,0,0]
        self.coords = self.get_all_cords()

    def get_all_cords(self):
        coords=[]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    coordscalc1=[self.a1[0]+i*self.a, self.a1[1]+j*self.a,self.a1[2]+k*self.a]
                    coordscalc2=[self.a2[0]+i*self.a,self.a2[1]+j*self.a,self.a2[2]+k*self.a]
                    coordscalc3=[self.a3[0]+i*self.a,self.a3[1]+j*self.a,self.a3[2]+k*self.a]
                    coordscalc4=[self.a4[0]+i*self.a,self.a4[1]+j*self.a,self.a4[2]+k*self.a]
                    
                    coords.append(coordscalc1)
                    coords.append(coordscalc2)
                    coords.append(coordscalc3)
                    coords.append(coordscalc4)
        return coords