# nbviewer-provider

Replaces all of the default providers in nbviewer with a simple URL rewrite for input of the form
`https://mindtrove.info/<name>` that renders a vanilla HTML page naming the page you entered. (You
have to use your imagination about what it might do instead.)

With docker installed, run:

```
make nbviewer
open http://localhost:8080
```

See the Dockerfile for how the provider is specified on the nbviewer command line.
