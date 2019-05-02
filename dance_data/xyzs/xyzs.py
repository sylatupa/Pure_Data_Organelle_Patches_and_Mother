if True:
    import os, sys
    #sys.path("PYTHONPATH") = []
    
    sys.path.append('../network')
    print(sys.path)
    user_paths = os.environ
    #print(user_paths)

    __import__("network.UDP") 
    UDP.send_line(1)
if __name__=="__main__":
    print(__name__)
    pass
