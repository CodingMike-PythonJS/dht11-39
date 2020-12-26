makerbit.connect_lcd(39)

def on_forever():
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P0, True, False, True)
    basic.show_string("T = ")
    basic.show_number(dht11_dht22.read_data(dataType.TEMPERATURE))
    basic.show_string("H =")
    basic.show_number(dht11_dht22.read_data(dataType.HUMIDITY))
    makerbit.show_string_on_lcd1602("T =" + str(dht11_dht22.read_data(dataType.TEMPERATURE)) + "*C",
        makerbit.position1602(LcdPosition1602.POS1),
        16)
    makerbit.show_string_on_lcd1602("H =" + str(dht11_dht22.read_data(dataType.HUMIDITY)) + "%",
        makerbit.position1602(LcdPosition1602.POS17),
        16)
basic.forever(on_forever)
