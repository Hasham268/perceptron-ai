with open('task.csv','r') as f:
    res = []
    for l in f:
        r = l.split(',')
        res.append(r)

    bp = []
    for l in res:
        bp.append(l[2])
    
    outcome = []
    for l in res:
        outcome.append(l[8])
        
    age = []
    for l in res:
        age.append(l[7])

    st = []
    for l in res:
        st.append(l[3])

    #70% data
    bloodPressure = []
    a = []
    skin = []
    actual = []
    for i in range(1, 490):
        bloodPressure.append(bp[i])
        a.append(age[i])
        skin.append(st[i])
        actual.append(outcome[i])
    final = []
    final.append(bloodPressure)
    final.append(a)
    final.append(skin)
    final.append(actual)

    w1 = 0.5
    w2 = 0.5
    w3 = 0.5

    x1a = final[0]
    x2a = final[1]
    x3a = final[2]
    ac = final[3]
    a = int(len(x1a))

    def wc(w, actual, output, x):
        wNew = w + (0.2 * (actual - output)* x)
        return wNew
    
    for i in range(a):
        output = 0
        
        while output != ac[i]:
            
            acc = (w1*int(x1a[i])) + (w2*int(x2a[i])) + (w3*int(x3a[i]))
            
            if (acc<120):
                output = 0
                z = 40
                while z!=0:
                    w1 = wc(float(w1), float(ac[i]), float(output), float(x1a[i]))
                    w2 = wc(float(w2), float(ac[i]), float(output), float(x2a[i]))
                    w3 = wc(float(w3), float(ac[i]), float(output), float(x3a[i]))
                    z=z-1
                if (z==0):
                    break
            elif (acc>120):
                output = 1
                w1 = 0.5
                w2 = 0.5
                w3 = 0.5

            if (output == 1):
               print('Patient', i+1, 'is Diabetic')
               
               print()
               break
