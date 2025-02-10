# docsforadobe.dev MkDocs Config

This repo holds the common components shared between this org's hosted MkDocs documentation projects.

The idea is that this repo will be kept up-to-date with global config, and each child repo will use the provided script to download the latest commit from this repo, and have its "local" MkDocs config point to the downloaded files from this repo.

In all cases, each child repo will be able to *override* config items here as needed.

## Updating This Repo

See [Modifying Common Components](https://docsforadobe.dev/contributing/common-components/modifying-common-components/) in the org contribution guide for info on how this repo works, and best practices for modifying it.
