from gpiozero import CPUTemperature

while True:
	cpu = CPUTemperature()
	print(cpu.temperature)
