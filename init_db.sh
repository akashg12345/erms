mysql -u root --password="1991"  << EOF
USE ${ERMS};
GRANT ALL PRIVILEGES ON  test_${ERMS}.* TO '${root}';
EOF