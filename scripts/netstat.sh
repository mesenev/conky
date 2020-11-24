lines=$(ss -ntup |head -8 |tail -n +2 |awk '{print $1 ";" $6 ";" $7 " "}')
for string in $lines
do
  arrIN=(${string//;/ })
  spaces=$(head -c "$((22 - ${#arrIN[1]}))" < /dev/zero | tr '\0' ' ')
  name=$(echo "${arrIN[2]}" |grep -o '".*"' |sed 's/"//g')
  printf "%s\t%s %s %s\n" "${arrIN[0]}" "${arrIN[1]}" "$spaces" "$name"
done
