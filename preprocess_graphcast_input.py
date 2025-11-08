import xarray as xr
import os

# Chemin des fichiers
input_surface_0000 = "era5_surface_0000.nc"
input_upper_0000 = "era5_upper_0000.nc"
input_surface_1800 = "era5_surface_1800.nc"
input_upper_1800 = "era5_upper_1800.nc"

# Vérifie que les fichiers existent
for f in [input_surface_0000, input_upper_0000, input_surface_1800, input_upper_1800]:
    if not os.path.exists(f):
        raise FileNotFoundError(f"Le fichier {f} est introuvable !")

# Ouvre les datasets avec xarray
ds_surface_0000 = xr.open_dataset(input_surface_0000, engine="netcdf4")
ds_upper_0000 = xr.open_dataset(input_upper_0000, engine="netcdf4")
ds_surface_1800 = xr.open_dataset(input_surface_1800, engine="netcdf4")
ds_upper_1800 = xr.open_dataset(input_upper_1800, engine="netcdf4")


# Combine les variables de surface et d'altitude pour chaque heure
ds_0000 = xr.merge([ds_surface_0000, ds_upper_0000])
ds_1800 = xr.merge([ds_surface_1800, ds_upper_1800])

# Combine les deux timestamps (T-6h et T0)
combined = xr.concat([ds_0000, ds_1800], dim="time")

# Sauvegarde au format Zarr (format GraphCast)
output_path = "era5_afrique_ouest_preprocessed.zarr"
combined.to_zarr(output_path, mode="w")

print(f"✅ Prétraitement terminé avec succès ! Fichier sauvegardé : {output_path}")
print(combined)
