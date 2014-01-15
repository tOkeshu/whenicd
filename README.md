When I cd
=========

`whenicd` executes your custom scripts when changing directory.

Getting Started
---------------

Download the project:

    $ git clone https://github.com/tOkeshu/whenicd.git

Install `whenicd.py`:

    $ cd /usr/bin
    # ln -s /path/to/whenicd.py

Modify your `.bashrc` to load the alias of the `cd` command:

    $ echo "source /path/to/whenicd.sh" >> ~/.bashrc

Reload your current shell and create your first `.cdrc`:

    $ bash
    $ cd ~/
    $ echo 'echo SUCCESS!!!' > .cdrc
    [whenicd] The hash for /home/user/.cdrc has changed! Still execute? [y,N,i,?]i
    == Content of /home/user/src/whenicd/.cdrc ==
    >  echo SUCCESS!!!
    == End of /home/freddy/user/whenicd/.cdrc ==
    [whenicd] The hash for /home/user/.cdrc has changed! Still execute? [y,N,i,?]y
    $ cd ~/
    SUCCESS!!!

License
-------

`whenicd` is realeased under the terms of the
[GNU General Public License v3](http://www.gnu.org/licenses/gpl.html)
or later.
