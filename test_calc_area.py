from pytest import approx, raises


def test_calc_area_rectangle():
    from calac_area import calc_area_rectangle
    assert calc_area_rectangle(2, 2) == 4
    assert calc_area_rectangle(2, 1) == 2
    
    
def test_calc_area_circle():
    from calac_area import calc_area_circle

    assert calc_area_circle(2) == approx(12.5663, abs=1e-3)

def test_calc_area_circle_errors():
    from calac_area import calc_area_circle

    with raises(ValueError):
        calc_area_circle(-1.0)

    with raises(TypeError):
        calc_area_circle('this is not a number')