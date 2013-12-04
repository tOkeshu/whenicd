function cd {
    args=$*
    builtin cd $args
    ret=$?
    env whenicd.py $args
    return $ret
}

