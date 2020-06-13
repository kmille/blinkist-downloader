#!/bin/bash
set -eux
input_file=$1
output_file=$2
sox "$input_file" "$output_file" tempo 0.8
