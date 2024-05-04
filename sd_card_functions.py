import board
import sdcardio
import storage
import os

def sd_mount_append_unmount(filename: str, data: str, header: str):
    try:
        spi = board.SPI()
        cs = board.D10
        sdcard = sdcardio.SDCard(spi, cs)
        vfs = storage.VfsFat(sdcard)
        storage.mount(vfs, "/sd")

        try:
            os.stat("/sd/%s" % filename)
        except Exception as _:
            with open(file="/sd/%s" % filename, mode="w", encoding="utf-8") as f:
                f.write(header)

        with open(file="/sd/%s" % filename, mode="a", encoding="utf-8") as f:
            f.write(data)

        storage.umount("/sd")
    except Exception as _:
        raise
    finally:
        sdcard.deinit()
        spi.deinit()
