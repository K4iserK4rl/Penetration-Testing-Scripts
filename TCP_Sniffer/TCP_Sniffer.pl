# TCP_Sniffer: creates a listening socket on the TCP port and prints out the headers of the packets received

=head1 NAME
=head2 SYNOPSIS

# Start traffic on the TCP Port via 
# > ping google.com

# Start listening by running the program

=cut

use autodie;
use strict;
use warnings;
use Socket ':all';
use NetPacket::IP;

my $tcp_port = getservbyname('echo', 'tcp');
my %protocol_map = qw(1 ICMP 6 TCP 17 UDP);

# Bind a socket to TCP port
socket(my $sniffer, AF_INET, SOCK_RAW, IPPROTO_ICMP);
setsockopt($sniffer, IPPROTO_IP, IP_HDRINCL, 1);
bind($sniffer, pack_sockaddr_in($tcp_port, INADDR_ANY));

# Continually check socket for received packets and use NetPacket::IP to decode
while(1) {
    if(recv($sniffer, my $received_bytes, 65565, 0)) {
        my $ip = NetPacket::IP->decode($received_bytes);

        printf("Protocol %s %s -> $s\n"),
            ($protocol_map{$ip->{proto} or 'Unknown'}),
            $ip->{src_ip},
            $ip->{dest_ip};
    }
}