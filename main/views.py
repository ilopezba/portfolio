from django.http import HttpResponse
from django.http import Http404
from django.template import Context
from django.shortcuts import render
from main.models import Page, Section, Image, ImageVersion
import os
from django.core.servers.basehttp import FileWrapper


def index(request):
    pages = Page.objects.all()
    context = Context({
        'pages': pages
    })
    return render(request, 'main/index.html', context)


def page(request, pageslug):
    try:
        page = Page.objects.get(slug=pageslug)
        sections = Section.objects.filter(page=page)
        # recopilamos las imagenes a previsualizar dentro de cada seccion
        for section in sections:
            images = Image.objects.filter(section=section, show_in_preview=True)
            for image in images:
                #si no hay ninguna version de la imagen pues nada
                versions = ImageVersion.objects.filter(image=image)
                if versions.__len__() > 0:
                    image.preview = ImageVersion.objects.filter(image=image)[0].thumbnail_image
            section.images = images

        pages = Page.objects.all()
        context = Context({
            'pages': pages,
            'sections': sections,
            'currentPage': page
        })
        return render(request, 'main/page.html', context)
    except Page.DoesNotExist:
        raise Http404


def section(request, pageslug, sectionslug):
    response = HttpResponse()
    try:
        page = Page.objects.get(slug=pageslug)
        section = Section.objects.get(slug=sectionslug)
        # section is inside page?
        if section.page == page:
            if section.content_type == 'images':
                # recopilamos todas las imagenes de esta seccion
                images = Image.objects.filter(section=section)
                for image in images:
                    #si no hay ninguna version de la imagen pues nada
                    versions = ImageVersion.objects.filter(image=image)
                    if versions.__len__() > 0:
                        image.preview = ImageVersion.objects.filter(image=image)[0].thumbnail_image
                section.images = images

                #render image section template
                pages = Page.objects.all()
                context = Context({
                    'pages': pages,
                    'currentPage': page,
                    'section': section
                })
                return render(request, 'main/section_images.html', context)
        else:
            response.write("<p>Section <b>%s</b> is not inside page <b>%s</b>.</p>" % (sectionslug, pageslug))

    except Page.DoesNotExist:
        response.write("<p>Page <b>%s</b> does not exist.</p>" % pageslug)
    except Section.DoesNotExist:
        response.write("<p>Section <b>%s</b> does not exist.</p>" % sectionslug)

    return response


def item(request, pageslug, sectionslug, itemslug):
    response = HttpResponse()
    try:
        page = Page.objects.get(slug=pageslug)
        section = Section.objects.get(slug=sectionslug)
        # section is inside page?
        if section.page == page:
            if section.content_type == 'images':
                image = Image.objects.get(slug=itemslug)
                if image.section == section:
                    versions = ImageVersion.objects.filter(image=image)
                    image.versions = versions

                    #render image section template
                    pages = Page.objects.all()
                    context = Context({
                        'pages': pages,
                        'currentPage': page,
                        'section': section,
                        'image': image
                    })
                    return render(request, 'main/image.html', context)
                else:
                    response.write("<p>Image <b>%s</b> is not inside section <b>%s</b>.</p>" % (itemslug, sectionslug))
        else:
            response.write("<p>Section <b>%s</b> is not inside page <b>%s</b>.</p>" % (sectionslug, pageslug))

    except Page.DoesNotExist:
        response.write("<p>Page <b>%s</b> does not exist.</p>" % pageslug)
    except Section.DoesNotExist:
        response.write("<p>Section <b>%s</b> does not exist.</p>" % sectionslug)
    except Image.DoesNotExist:
        response.write("<p>Image <b>%s</b> does not exist.</p>" % itemslug)

    return response


def download(request, pageslug, sectionslug, itemslug, versionid):
    """
    Send a file through Django without loading the whole file into
    memory at once. The FileWrapper will turn the file object into an
    iterator for chunks of 8KB.
    """
    response = HttpResponse()
    try:
        page = Page.objects.get(slug=pageslug)
        section = Section.objects.get(slug=sectionslug)
        # section is inside page?
        if section.page == page:
            if section.content_type == 'images':
                image = Image.objects.get(slug=itemslug)
                if image.section == section:
                    version = ImageVersion.objects.get(id=versionid)
                    if version.image == image:
                        # TODO check if the user can download this file
                        filename = version.original_image._get_path()
                        wrapper = FileWrapper(file(filename))
                        response = HttpResponse(wrapper, content_type='text/plain')
                        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
                        response['Content-Length'] = os.path.getsize(filename)
                        return response
                    else:
                        response.write("<p>Image Version <b>%s</b> is not a version of <b>%s</b>.</p>" % (versionid, itemslug))
                else:
                    response.write("<p>Image <b>%s</b> is not inside section <b>%s</b>.</p>" % (itemslug, sectionslug))
        else:
            response.write("<p>Section <b>%s</b> is not inside page <b>%s</b>.</p>" % (sectionslug, pageslug))

    except Page.DoesNotExist:
        response.write("<p>Page <b>%s</b> does not exist.</p>" % pageslug)
    except Section.DoesNotExist:
        response.write("<p>Section <b>%s</b> does not exist.</p>" % sectionslug)
    except Image.DoesNotExist:
        response.write("<p>Image <b>%s</b> does not exist.</p>" % itemslug)
    except ImageVersion.DoesNotExist:
        response.write("<p>Image Version <b>%s</b> does not exist.</p>" % versionid)

    return response

