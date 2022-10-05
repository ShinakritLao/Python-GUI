#b-ifelse.py

friend = 'จอห์น'

print('เงื่อนไข 1:', friend == 'จอห์น')
print('เงื่อนไข 2:', friend == 'ฌอน')


if friend == 'จอห์น':
	print('Hi, ' + friend)
elif friend == 'ฌอน':
	print('สวัสดีครับ, ' + friend)
elif friend == 'สมศรี':
	print('สวัสดีครับป้า, ' + friend)
else:
	print('สวัสดีคุณ' + friend)

