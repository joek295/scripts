#!/bin/sh

# Show terminal colors.

# From LinuxBBQ

# <esc>[..m sequences set colour.

# First we must check whether we are using dash or bash as sh as they
# treat echo differently.  Bash requires the flag -e for escapes,
# while dash assumes that \ is used as an escape by default.

# Note that this assumes that all non-dash shells behave like bash.
# This *should* be true, because bash's behaviour is POSIXly correct.
# However, it may not be, in which case this script may break.

SH=`readlink /bin/sh`
if [ $SH = "dash" ]; then
  ECHO="echo"
else
  ECHO="echo -e"
fi

# now print the colours
echo "                  ANSI TERMINAL COLOR TABLE                        "

$ECHO "BRIGHTER  \033[30;1m black \033[31;1m red \033[32;1m green \033[33;1m yellow \033[34;1m blue \033[35;1m purple \033[36;1m cyan \033[37;1m white \033[0m\n"
$ECHO "          \033[40;1m black \033[41;1m red \033[42;1m green \033[43;1m yellow \033[44;1m blue \033[45;1m purple \033[46;1m cyan \033[47;1m white \033[0m\n"

$ECHO "DIMMER    \033[30;2m black \033[31;2m red \033[32;2m green \033[33;2m yellow \033[34;2m blue \033[35;2m purple \033[36;2m cyan \033[37;2m white \033[0m\n"
$ECHO "          \033[40;2m black \033[41;2m red \033[42;2m green \033[43;2m yellow \033[44;2m blue \033[45;2m purple \033[46;2m cyan \033[47;2m white \033[0m\n"

$ECHO "UNDERLINE \033[30;4m black \033[31;4m red \033[32;4m green \033[33;4m yellow \033[34;4m blue \033[35;4m purple \033[36;4m cyan \033[37;4m white \033[0m\n"
$ECHO "          \033[40;4m black \033[41;4m red \033[42;4m green \033[43;4m yellow \033[44;4m blue \033[45;4m purple \033[46;4m cyan \033[47;4m white \033[0m\n"

$ECHO "FLASHING  \033[30;5m black \033[31;5m red \033[32;5m green \033[33;5m yellow \033[34;5m blue \033[35;5m purple \033[36;5m cyan \033[37;5m white \033[0m\n"
$ECHO "          \033[40;5m black \033[41;5m red \033[42;5m green \033[43;5m yellow \033[44;5m blue \033[45;5m purple \033[46;5m cyan \033[47;5m white \033[0m\n"

$ECHO "REVERSE   \033[30;7m black \033[31;7m red \033[32;7m green \033[33;7m yellow \033[34;7m blue \033[35;7m purple \033[36;7m cyan \033[37;7m white \033[0m\n"
$ECHO "          \033[40;7m black \033[41;7m red \033[42;7m green \033[43;7m yellow \033[44;7m blue \033[45;7m purple \033[46;7m cyan \033[47;7m white \033[0m"
