import time
import board 
#import alarm
import microcontroller
import supervisor
import digitalio
#import neopixel

#pixel = neopixel.NeoPixel(board.NEOPIXEL, 1 , pixel_order=neopixel.RGB)
#pixel[0] = (180, 0, 255)
#pixel.write()

#neopix = digitalio.DigitalInOut(board.NEOPIXEL)
#neopix.direction = digitalio.Direction.OUTPUT

#neopixel_write.neopixel_write(neopix, bytearray([180, 0, 255]))
microcontroller.reset()

if supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.BROWNOUT:
    #time_alarm = alarm.time.TimeAlarm(monotonic_time = time.monotonic + 10*60)
    #alarm.exit_and_deep_sleep_until_alarms(time_alarm)
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.GC_ALLOC_OUTSIDE_VM:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.FLASH_WRITE_FAIL:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.HARD_FAULT:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.INTERRUPT_ERROR:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.NLR_JUMP_FAILED:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.NO_HEAP:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.SDK_FATAL_ERROR:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.WATCHDOG:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.NO_CIRCUITPY:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.STACK_OVERFLOW:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.USB_TOO_MANY_ENDPOINTS:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.USB_TOO_MANY_INTERFACE_NAMES:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.USB_BOOT_DEVICE_NOT_INTERFACE_ZERO:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.SAFE_MODE_PY_ERROR:
    microcontroller.reset()

elif supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.PROGRAMMATIC:
    microcontroller.reset()

else:
    microcontroller.reset()
    
