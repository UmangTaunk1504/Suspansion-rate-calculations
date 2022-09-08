from cmath import cos, pi

def MotionRatio():
    print('a is the distance between lower mounting point of damper and wishbone with frame')
    a = float(input("Enter value of a: ")) #a is the distance between lower mounting point of damper and wishbone with frame
    print('b is the distance between mounting of lower wishbone with frame and lower knuckle joint')
    b = float(input("Enter value of b: ")) #b is the distance between mounting of lower wishbone with frame and lower knuckle joint
    # Always a<b 
    if a<b:
        m = a/b #formula for motion ratio
        return m
    else:
        return print('Wrong values!!, Always a<b')

def RideRate():
    fr = float(input('Enter ride frquency: ')) #Ride Frequency
    Sm = float(input('Enter Sprung mass: ')) #Sprung Mass on 1 wheel
    rr = (fr**2)*Sm #formula for ride rate
    return rr

def WheelRate():
    kr = RideRate()
    tr = float(input('Tire Rate: '))  #Tire rate is given in tire data
    wr = kr*tr/(tr-kr) #formula for wheel rate
    return wr

def SpringRate():
    mr = MotionRatio()
    wr = WheelRate()
    theta = float(input('Enter Angle: ')) # angle made at lower mounting poinnt by the damper from verticle
    sr = wr/(mr**2*cos(theta*pi/180)) #formula for Spring rate
    return sr

print('''MR = Motion Ratio         SR = Spring Rate
WR = Wheel Rate           RR = Ride Rate''')
parameter = input("What you want? (MR, SR, WR, RR): ")

if parameter == 'MR':
    mr = MotionRatio()
    print(f'Motion Ratio is: {mr}')

elif parameter == 'RR':
    rr = RideRate()
    print(f'Ride Rate: {rr} N/m')

elif parameter == 'WR':
    wr = WheelRate()
    print(f'Wheel Rate: {wr} N/m')

elif parameter == 'SR':
    sr = SpringRate()
    print(f'Spring Rate: {sr.real} N/m')
