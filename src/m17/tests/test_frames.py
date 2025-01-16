"""
Test the encoding and decoding of M17 frames.
"""
import unittest


from m17.address import Address
from m17.misc import example_bytes
from m17.frames import LICHFrame, RegularFrame, IPFrame, M17Payload


class test_frame_encodings(unittest.TestCase):
    """
    Test the encoding and decoding of M17 frames.
    """
    def test_lich(self):
        """
        Test encoding and decoding of LICH frames.
        """
        lich = LICHFrame(
            dst=Address(callsign="SP5WWP"),
            src=Address(callsign="W2FBI"),
            stream_type=5,
            nonce=bytes(example_bytes(14)),
        )
        bl = bytes(lich)
        lich2 = LICHFrame.from_bytes(bl)
        assert lich == lich2

    def test_regular_frame(self):
        """
        Test encoding and decoding of regular frames.
        """
        lich = LICHFrame(
            dst=Address(callsign="SP5WWP"),
            src=Address(callsign="W2FBI"),
            stream_type=5,
            nonce=example_bytes(14),
        )

        m17_payload = M17Payload(frame_number=1, payload=example_bytes(8))

        x = RegularFrame(lich=lich, m17_payload=m17_payload)
        y = bytes(x)
        z = RegularFrame.from_bytes(y)
        assert z == x

    def test_ip_frame(self):
        lich = LICHFrame(
            dst=Address(callsign="SP5WWP"),
            src=Address(callsign="W2FBI"),
            stream_type=5,
            nonce=example_bytes(14),
        )

        m17_payload = M17Payload(frame_number=1, payload=example_bytes(8))

        x = IPFrame(
            stream_id=0xf00d,
            full_lich=lich,
            m17_payload=m17_payload
        )
        y = bytes(x)
        z = IPFrame.from_bytes(y)
        assert z == x
