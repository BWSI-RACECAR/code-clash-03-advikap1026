class Solution:    
    def propcontrol(self, center, res):
            #type center: int
            #type res: tuples of int
            #return type: float
            
            #TODO: Write code below to return a float with the solution to the prompt.
            Kp = 4
            if center is not None: 
                 angle = Kp*(center[1]-(rc.camera.get_width()/2))
            else:
                 angle = 1 
            max = res[0]
            min = res[1]
            middle = (max + min)/2
            ans = middle - center 
            roundedAns = round(ans,6)
            pass
        
        

def main():
    center = int(input().strip())
    resx = int(input().strip())
    resy = int(input().strip())
    res = (resx, resy)

    tc1 = Solution()
    ans = tc1.propcontrol(center, res)
    ans=format(ans, ".6f")
    print(ans)

if __name__ and "__main__":
    main()
