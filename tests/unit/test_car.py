

class TestCar:
    def test_car_starts_with_fuel(self, car, engine_mock):
        result = car.start()
        assert result == "Engine started"
        engine_mock.start.assert_called_once()

    def test_car_does_not_start_without_fuel(self, car, fuel_system_mock, engine_mock):
        fuel_system_mock.fuel_level = 0
        result = car.start()
        assert result == "Cannot start, no fuel"
        engine_mock.start.assert_not_called()

    def test_car_stops_engine(self, car, engine_mock):
        result = car.stop()
        assert result == "Engine stopped"
        engine_mock.stop.assert_called_once()

    def test_refuel_increases_fuel_level(self, fuel_system_mock):
        result = fuel_system_mock.refuel(10)
        assert result == "Fuel level: 20"
        fuel_system_mock.refuel.assert_called_once_with(10)
