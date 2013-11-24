#!/bin/bash

gst-launch-1.0 -v tcpclientsrc host=$1 port=5000 \
! gdpdepay ! rtph264depay ! avdec_h264 ! videoflip method=horizontal-flip ! videoconvert ! autovideosink sync=false
