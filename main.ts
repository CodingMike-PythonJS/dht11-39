makerbit.connectLcd(39)
basic.forever(function () {
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P0,
    true,
    false,
    true
    )
    basic.showString("T = ")
    basic.showNumber(dht11_dht22.readData(dataType.temperature))
    basic.showString("H =")
    basic.showNumber(dht11_dht22.readData(dataType.humidity))
    makerbit.showStringOnLcd1602("T =" + dht11_dht22.readData(dataType.temperature) + "*C", makerbit.position1602(LcdPosition1602.Pos1), 16)
    makerbit.showStringOnLcd1602("H =" + dht11_dht22.readData(dataType.humidity) + "%", makerbit.position1602(LcdPosition1602.Pos17), 16)
})
