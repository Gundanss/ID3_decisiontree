import pandas as pd

csv_data = pd.read_csv('forestfires.csv')
print(csv_data)

print(csv_data['area'] == 0)
print(csv_data['area'].dtypes)

csv_data.X[(csv_data['X'] <= 5) & (csv_data['Y'] <= 5)] = 0
csv_data.X[(csv_data['X'] > 5) & (csv_data['Y'] <= 5)] = 1
csv_data.X[(csv_data['X'] <= 5) & (csv_data['Y'] > 5)] = 2
csv_data.X[(csv_data['X'] > 5) & (csv_data['Y'] > 5)] = 3
print(csv_data)
csv_data['X'] = csv_data['X'].astype(str)
print(csv_data.area)
# csv_data['area'] = csv_data['area'].replace('0.0', 'no')
# csv_data['area'] = csv_data['area'].replace('1.0', 'yes')
csv_data['X'] = csv_data['X'].replace('0', 'southwest')
csv_data['X'] = csv_data['X'].replace('1', 'southeast')
csv_data['X'] = csv_data['X'].replace('2', 'northwest')
csv_data['X'] = csv_data['X'].replace('3', 'northeast')
print(csv_data)



# replace value:1 is on fire and 0 is not on fire
csv_data.area[csv_data['area'] <= 0] = 0
csv_data.area[csv_data['area'] > 0] = 1
# csv_data.area[csv_data['area'] <= 0] = 0
# csv_data.area[(csv_data['area'] > 0) & (csv_data['area'] <= 4)] = 1
# csv_data.area[csv_data['area'] > 4] = 2
print(csv_data)
#change type to object
csv_data['area'] = csv_data['area'].astype(str)
print(csv_data.area)
csv_data['area'] = csv_data['area'].replace('0.0', 'no')
csv_data['area'] = csv_data['area'].replace('1.0', 'yes')
# csv_data['area'] = csv_data['area'].replace('0.0', 'no')
# csv_data['area'] = csv_data['area'].replace('1.0', 'small')
# csv_data['area'] = csv_data['area'].replace('2.0', 'big')
print(csv_data)

#replace the rain value. change to nominal value.
csv_data.rain[csv_data['rain'] <= 0 ] = 0
csv_data.rain[csv_data['rain'] > 0 ] = 1
csv_data['rain'] = csv_data['rain'].astype(str)
csv_data['rain'] = csv_data['rain'].replace('0.0', 'no')
csv_data['rain'] = csv_data['rain'].replace('1.0', 'yes')
# print(csv_data)

#replace the wind value. change to nominal value based on average value
csv_data.wind[csv_data['wind'] <= 4.02 ] = 0
csv_data.wind[csv_data['wind'] > 4.02 ] = 1
csv_data['wind'] = csv_data['wind'].astype(str)
csv_data['wind'] = csv_data['wind'].replace('0.0', 'low')
csv_data['wind'] = csv_data['wind'].replace('1.0', 'high')
# print(csv_data)

#replace the RH value. change to nominal value based on average value
csv_data.RH[csv_data['RH'] <= 44.29 ] = 0
csv_data.RH[csv_data['RH'] > 44.29 ] = 1
csv_data['RH'] = csv_data['RH'].astype(str)
csv_data['RH'] = csv_data['RH'].replace('0', 'low')
csv_data['RH'] = csv_data['RH'].replace('1', 'high')
# print(csv_data)

#replace the temp value. change to nominal value based on average value
csv_data.temp[csv_data['temp'] <= 18.89 ] = 0
csv_data.temp[csv_data['temp'] > 18.89 ] = 1
csv_data['temp'] = csv_data['temp'].astype(str)
csv_data['temp'] = csv_data['temp'].replace('0.0', 'low')
csv_data['temp'] = csv_data['temp'].replace('1.0', 'high')
# print(csv_data)

#replace the ISI value. change to nominal value based on average value
csv_data.ISI[csv_data['ISI'] <= 9.02 ] = 0
csv_data.ISI[csv_data['ISI'] > 9.02 ] = 1
csv_data['ISI'] = csv_data['ISI'].astype(str)
csv_data['ISI'] = csv_data['ISI'].replace('0.0', 'low')
csv_data['ISI'] = csv_data['ISI'].replace('1.0', 'high')
# print(csv_data)

#replace the FFMC value. change to nominal value based on average value
csv_data.FFMC[csv_data['FFMC'] <= 90.64 ] = 0
csv_data.FFMC[csv_data['FFMC'] > 90.64 ] = 1
csv_data['FFMC'] = csv_data['FFMC'].astype(str)
csv_data['FFMC'] = csv_data['FFMC'].replace('0.0', 'low')
csv_data['FFMC'] = csv_data['FFMC'].replace('1.0', 'high')
# print(csv_data)

#replace the DC value. change to nominal value based on average value
csv_data.DC[csv_data['DC'] <= 437.7] = 0
csv_data.DC[(csv_data['DC'] > 437.7) & (csv_data['DC'] <= 664.2)] = 1
csv_data.DC[(csv_data['DC'] > 664.2) & (csv_data['DC'] <= 713.9)] = 2
csv_data.DC[csv_data['DC'] > 713.9] = 3
# csv_data.DC[csv_data['DC'] <= 547.9] = 0
# csv_data.DC[csv_data['DC'] > 547.9] = 1
csv_data['DC'] = csv_data['DC'].astype(str)
# csv_data['DC'] = csv_data['DC'].replace('0.0', 'low')
# csv_data['DC'] = csv_data['DC'].replace('1.0', 'high')
csv_data['DC'] = csv_data['DC'].replace('0.0', 'low')
csv_data['DC'] = csv_data['DC'].replace('1.0', 'mid')
csv_data['DC'] = csv_data['DC'].replace('2.0', 'high')
csv_data['DC'] = csv_data['DC'].replace('3.0', 'veryhigh')
print(csv_data)
print(csv_data.iloc[[156], :])

# #replace the DMC value. change to nominal value based on average value
# csv_data.DMC[csv_data['DMC'] <= 68.6] = 0
# csv_data.DMC[(csv_data['DMC'] > 68.6) & (csv_data['DMC'] <= 108.3)] = 1
# csv_data.DMC[(csv_data['DMC'] > 108.3) & (csv_data['DMC'] <= 142.4)] = 2
# csv_data.DMC[csv_data['DMC'] > 142.4] = 3
csv_data.DMC[csv_data['DMC'] <= 110.9] = 0
csv_data.DMC[csv_data['DMC'] > 110.9] = 0
csv_data['DMC'] = csv_data['DMC'].astype(str)
csv_data['DMC'] = csv_data['DMC'].replace('0.0', 'low')
csv_data['DMC'] = csv_data['DMC'].replace('1.0', 'high')
print(csv_data)
print(csv_data.iloc[[156], :])


# csv_data.to_csv("modified.csv")
csv_data.to_csv("modified4.0.csv")



