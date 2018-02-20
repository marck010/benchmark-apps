# FROM microsoft/dotnet:runtime
# VOLUME [ "./","/opt/my-app-netcore" ]
# WORKDIR /opt/my-app-netcore
# CMD ["/bin/sh","export NODE_ENV='production' && dotnet run --configuration Release"]

FROM microsoft/dotnet:sdk AS build-env
WORKDIR /opt/my-app-netcore
COPY . ./
RUN dotnet restore
RUN dotnet publish -c Release -o out

FROM microsoft/dotnet:runtime
WORKDIR /opt/my-app-netcore
COPY --from=build-env /opt/my-app-netcore/out ./
ENTRYPOINT ["dotnet", "my-app-netcore.dll"]