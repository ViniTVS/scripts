#!/bin/bash
TILED_DESKTOP_ID=$(bspc query -D -d '^4')

bspc subscribe node_add | while read -a msg ; do
	desk_id=${msg[3]}
	wid=${msg[4]}
	[ "$TILED_DESKTOP_ID" = "$desk_id" ] || bspc node "$wid" -t floating
done

TILED_DESKTOP_ID=$(bspc query -D -d '^5')

bspc subscribe node_add | while read -a msg ; do
	desk_id=${msg[3]}
	wid=${msg[4]}
	[ "$TILED_DESKTOP_ID" = "$desk_id" ] || bspc node "$wid" -t floating
done