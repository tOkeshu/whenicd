function cd {
    args=$*
    builtin cd $args
    ret=$?
    if [ $ret -ne 0 ]; then
     return $ret
     fi
    env whenicd.py $args
    return $ret
}