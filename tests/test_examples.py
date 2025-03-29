from aigerox import Aig

def test_load_and():
    aig = Aig.from_file("data/examples/and.aag")
    print(aig)
    assert len(aig.inputs()) == 2
    assert len(aig.outputs()) == 1
    assert len(aig.and_gates()) == 1

def test_load_buffer():
    aig = Aig.from_file("data/examples/buffer.aag")
    print(aig)
    assert len(aig.inputs()) == 1
    assert len(aig.outputs()) == 1
    assert len(aig.and_gates()) == 0

def test_load_halfadder():
    aig = Aig.from_file("data/examples/halfadder.aag")
    print(aig)
    assert len(aig.inputs()) == 2
    assert len(aig.outputs()) == 2
    assert len(aig.and_gates()) == 3
