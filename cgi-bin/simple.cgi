#! /bin/bash

# This is a little CGI program


###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The MIME type of associated with the option body of the HTTP request.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAY_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.  
# HTTP_USER_AGENT:   Information about the browser/client that made requested.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. The most common methods are GET and POST.
# REQUEST_URI:       The URI of the request
# SERVER_PROTOCOL:   Currently HTTP/1.1
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address
# SERVER_PORT:       The port of the server


#      Added a content type and a blank line

echo "X-Cit-160: hello again steve!"
if [ $QUERY_STRING = "HTML" ] ; then
    echo "Content-type: text/html"
else
    echo "Content-type: text/plain"
fi
if [ -n "${QUERY_STRING}" ] ; then
    echo "Content-type: text/html"
fi

echo ""

echo "Request method: $REQUEST_METHOD"
echo "Query string: $QUERY_STRING"
echo "Script name: $SCRIPT_NAME"
echo "Request URI: $REQUEST_URI"
echo ""

# Get response
if [ $REQUEST_METHOD = "GET" ] ; then
    echo "This is a get."
fi

# Separate URI
if [ "$SCRIPT_NAME/password" = $REQUEST_URI ] ; then
    echo "The password is '123'."
fi

# HTML return
if [ $QUERY_STRING = "HTML" ] ; then
    cat ./simple.html
fi

# Reading from system information and from another website
# If the query matches the form of a url then curl the url to file and return file
if [[ $QUERY_STRING =~ ^(http\:\/\/|https\:\/\/)?([a-z0-9][a-z0-9\-]*\.)+[a-z0-9][a-z0-9\-]*$ ]] ; then
	/usr/bin/curl ${QUERY_STRING} >htmlFile
	cat ./htmlFile
	
	cat ./header.html
	#TODO: Cat my header on top of the html
fi


if [ -n "${QUERY_STRING}" ] ; then
   cat  ./${QUERY_STRING}
fi

# Read the body -- if it is a post
while read _post_line ; do
  echo ${_post_line} ";loop"
done
echo $_post_line


exit 0
