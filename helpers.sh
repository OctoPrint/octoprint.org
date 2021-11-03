function get_nginx_var {
    VAR=$1
    CONFIG=$2

    grep "set \$$VAR" "$CONFIG" | awk -F " " '{$1=$3;gsub(/"/, "", $1);print substr($1, 1, length($1) - 1)}'
}

function set_nginx_var {
    VAR=$1
    VALUE=$2
    CONFIG=$3

    sed -i "s@set \$$VAR .*@set \$$VAR \"$VALUE\";@g" "$CONFIG"
}