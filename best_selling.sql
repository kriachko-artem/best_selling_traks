DROP TABLE IF EXISTS best_selling_tracks;

CREATE TABLE best_selling_tracks AS
SELECT t.TrackId, t.Name as 'title', a2.Name as 'artist', COUNT(i.InvoiceId) as 'count' FROM tracks t
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists a2 ON a.ArtistId = a2.ArtistId
JOIN invoice_items ii ON t.TrackId = ii.TrackId
JOIN invoices i ON ii.InvoiceId = i.InvoiceId
GROUP BY i.InvoiceId;