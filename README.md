# clustir
Personal Content Archive Manager

## Artifact Specification

**File Pair**  
Each artifact is up to two files with the same base name (the SHA-256 hash of the content) but different extensions:
1. `<hash>.json` (the “header”)
2. `<hash>.bin` (optional “binary content”)

The `.json` describes the artifact, while the `.bin` holds optional raw bytes/blobs.

### 1. Header (`.json`)

The JSON file contains the metadata, including values needed to interpret the `.bin` content. When a bin is present it can include:

```jsonc
{
  "type": "mime/type",         // MIME type, e.g. "text/plain", "image/png", etc.
  "size": 1234,                // Size of the binary content in bytes
  "hash": "sha256...",         // SHA-256 hash of the binary content
  "time": 1737232722.8340352,  // When created/saved
  "text": "optional"           // Optional text version of the bin. For `application/x-file`, contains filename
}
```

- **type**: The MIME type of the bin content (see list of supported types below).  
- **size**: The exact size of the `.bin` file in bytes.  
- **hash**: The full SHA-256 (hex) hash of the `.bin` file’s contents.  
- **time**: When the artifact was initially created/saved
- **text** (optional):  
  - For text-based MIME types (e.g., `text/plain`), it may store a short textual representation of the content.  
  - For `application/x-file`, this field is the original filename (or any relevant display name).  
  - For other data (e.g., images), this field may be omitted or used for an additional description.

> **Implementation note**: The header can also include other fields as desired.

### 2. Optional Binary Message (`.bin`)

- This file contains raw binary data corresponding to the header.  
- The length in bytes must match the `size` field from the JSON header.  
- The SHA-256 digest of the file must match the `hash` field in the JSON header.  
- To reconstruct or process the binary data, read and parse the header first (`.json`), then apply the metadata to interpret the corresponding `.bin`.

## Supported MIME Types

The following MIME types have been identified:

- **text/plain**: Plain text content.  
- **text/html**: HTML content.  
- **text/rtf**: Rich Text Format content.  
- **image/png**: PNG images.  
- **application/x-file**: Any other files (the header’s `"text"` indicates the filename).

Additional MIME types can be supported if needed, provided they follow the same JSON/binary convention above.
