import json
from statistics import mean, mode, variance, stdev, median, StatisticsError


def writeJson():

    xn = {}
    tn = {}
    cn = {}
    with open("../assets/data/generated.json", "r") as rFile:
        data = json.load(rFile)
        cnMean = data['mean']
        cnVariance = data['variance']
        cnMedian = data['mode']
        cnStdev = data['stdev']
        cnMode = data['mode']
        xn['Sample'] = data['X']
        tn['Sample'] = data['Tk']
        cn['Sample'] = data['cost']
        rFile.close()
    # Xn analysis
    xnMean = mean(data['X'])
    xnVariance = variance(data['X'])
    xnMedian = median(data['X'])
    xnStdev = stdev(data['X'])

    # Tn analysis
    tnMean = mean(data['Tk'])
    tnVariance = variance(data['Tk'])
    tnMedian = median(data['Tk'])
    tnStdev = stdev(data['Tk'])

    try:
        xnMode = mode(data['X'])
        tnMode = mode(data['Tk'])
    except StatisticsError:
        xnMode = 0
        tnMode = 0

    xn['mean'] = xnMean
    xn['mode'] = xnMode
    xn['median'] = xnMedian
    xn['variance'] = xnVariance
    xn['stdev'] = xnStdev

    tn['mean'] = tnMean
    tn['mode'] = tnMode
    tn['median'] = tnMedian
    tn['variance'] = tnVariance
    tn['stdev'] = tnStdev

    cn['mean'] = cnMean
    cn['mode'] = cnMode
    cn['median'] = cnMedian
    cn['variance'] = cnVariance
    cn['stdev'] = cnStdev

    output = {"Xn": xn, "Tn": tn, "Cn": cn}

    with open("../assets/data/sort_data.json", "w") as wFile:
        json.dump(output, wFile, indent=4)


writeJson()
